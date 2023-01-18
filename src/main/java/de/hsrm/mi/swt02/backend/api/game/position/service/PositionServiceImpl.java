package de.hsrm.mi.swt02.backend.api.game.position.service;

import de.hsrm.mi.swt02.backend.api.game.position.repository.PositionRepository;
import de.hsrm.mi.swt02.backend.api.player.repository.PlayerRepository;
import de.hsrm.mi.swt02.backend.domain.game.position.PlayerPosition;
import de.hsrm.mi.swt02.backend.domain.player.Player;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
@Slf4j
public class PositionServiceImpl implements PositionService{
    @Autowired
    PositionRepository positionRepository;
    @Autowired
    PlayerRepository playerRepository;

    /**
     * @return list of all PlayerPosition
     */
    @Override
    public List<PlayerPosition> findAllPositions() {
        return positionRepository.findAll();
    }

    /**
     * @param id of PlayerPosition
     */
    @Override
    public void deletePosition(long id) {
        positionRepository.deleteById(id);
    }

    /**
     * @param player Player to be persisted
     * @param x Coordinate of Player on 3d world
     * @param y Coordinate of Player on 3d world
     * @return id of created Position
     */
    @Override
    @Transactional
    public long createPosition(Player player, double x, double y, double rotation) {
        PlayerPosition playerPosition = new PlayerPosition(player, x, y, rotation);
        player.setPlayerPosition(playerPosition);
        playerRepository.save(player);
        return positionRepository.save(playerPosition).getId();
    }

    /**
     * @param playerPositionId Player ID to be updated
     * @param x Coordinate of Player on 3d world
     * @param y Coordinate of Player on 3d world
     * @param rotation Rotation of Player on 3d world
     */
    @Override
    @Transactional
    public void savePosition(long playerPositionId, double x, double y, double rotation) {
        Optional<PlayerPosition> optionalPlayerPosition = positionRepository.findById(playerPositionId);
        if (optionalPlayerPosition.isPresent()) {
            var playerPosition = optionalPlayerPosition.get();
            playerPosition.setPosX(x);
            playerPosition.setPosY(y);
            playerPosition.setRotation(rotation);
            positionRepository.save(playerPosition);
        } else
            log.info("PlayerPosition:" + playerPositionId + " not found");
    }
}